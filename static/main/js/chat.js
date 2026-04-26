(function () {
    const root = document.getElementById('tatsuki-chat');
    if (!root) return;

    const log = root.querySelector('.chat-log');
    const form = root.querySelector('.chat-form');
    const input = root.querySelector('.chat-input');
    const sendBtn = root.querySelector('.chat-send');
    const csrfToken = root.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const endpoint = root.dataset.endpoint;

    const lang = (document.documentElement.lang || 'en').toLowerCase().startsWith('ja') ? 'ja' : 'en';
    const t = {
        greeting: root.dataset['greeting' + (lang === 'ja' ? 'Ja' : 'En')],
        thinking: root.dataset['thinking' + (lang === 'ja' ? 'Ja' : 'En')],
        errorMsg: root.dataset['error' + (lang === 'ja' ? 'Ja' : 'En')],
        placeholder: root.dataset['placeholder' + (lang === 'ja' ? 'Ja' : 'En')],
    };
    input.placeholder = t.placeholder;

    const history = [];
    let pending = false;
    let lastSentAt = 0;
    const MIN_INTERVAL_MS = 1000;

    function appendMessage(role, text, opts) {
        const wrap = document.createElement('div');
        wrap.className = 'chat-msg chat-msg--' + role + (opts && opts.muted ? ' chat-msg--muted' : '');
        const bubble = document.createElement('div');
        bubble.className = 'chat-bubble';
        bubble.textContent = text;
        wrap.appendChild(bubble);
        log.appendChild(wrap);
        log.scrollTop = log.scrollHeight;
        return wrap;
    }

    appendMessage('assistant', t.greeting);

    form.addEventListener('submit', async function (event) {
        event.preventDefault();
        if (pending) return;

        const now = Date.now();
        if (now - lastSentAt < MIN_INTERVAL_MS) return;

        const message = input.value.trim();
        if (!message) return;

        lastSentAt = now;
        pending = true;
        input.value = '';
        input.disabled = true;
        sendBtn.disabled = true;

        appendMessage('user', message);
        history.push({ role: 'user', content: message });

        const thinkingEl = appendMessage('assistant', t.thinking, { muted: true });

        try {
            const res = await fetch(endpoint, {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ messages: history }),
            });

            let data = {};
            try { data = await res.json(); } catch (_) { /* ignore */ }

            thinkingEl.remove();

            if (!res.ok) {
                const errText = data.error || t.errorMsg;
                appendMessage('assistant', errText, { muted: true });
                history.pop();
            } else {
                const reply = (data.reply || '').trim() || t.errorMsg;
                appendMessage('assistant', reply);
                history.push({ role: 'assistant', content: reply });
            }
        } catch (err) {
            thinkingEl.remove();
            appendMessage('assistant', t.errorMsg, { muted: true });
            history.pop();
        } finally {
            pending = false;
            input.disabled = false;
            sendBtn.disabled = false;
            input.focus();
        }
    });
})();
