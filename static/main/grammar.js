function checkGrammar() {
    const url = 'https://api.languagetoolplus.com/v2/check';
    const headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    };

    const data = new URLSearchParams({
        'text': document.getElementById("text").value,
        'language': 'en-US',
        'enabledOnly': 'false',
        'level': 'picky',
    });

    fetch(url, {
        method: 'POST',
        headers: headers,
        body: data,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error: ${response.status}, ${response.statusText}`);
        }
        return response.json();
    })
    .then(parsedData => {
        const matches = parsedData.matches;

        const formattedMatches = matches.map(match => ({
            message: match.message,
            shortMessage: match.shortMessage,
            replacements: match.replacements.map(replacement => replacement.value).slice(0, 5),
            context: match.context.text.slice(match.context.offset, match.context.offset + match.context.length),
        }));

        document.getElementById("issues").innerText = formattedMatches.map(e => `
${e.message}
${e.shortMessage}
The issue occurred in this context: "${e.context}"
-----------------------
Did you mean:
${e.replacements.map(x => "- " + x + "\n").join("")}
=======================`).join("");
})
    .catch(error => console.error(error));
}