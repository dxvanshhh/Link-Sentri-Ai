// --- CREATIVE BROWSER INTERACTION ---

// Listen for when the browser is about to navigate to a new page
chrome.webNavigation.onBeforeNavigate.addListener(async (details) => {
    // Ignore internal chrome pages and sub-frame navigations
    if (details.frameId !== 0 || !details.url.startsWith('http')) {
        return;
    }

    const url = details.url;
    console.log(`Scanning URL: ${url}`);

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url }),
        });
        const data = await response.json();

        // INNOVATIVE FEATURE: Change extension icon based on safety
        chrome.action.setIcon({
            path: data.result === 'dangerous' ? 'icons/icon-danger.png' : 'icons/icon-safe.png',
            tabId: details.tabId
        });

        if (data.result === 'dangerous') {
            // INNOVATIVE FEATURE: Use a rich, non-blocking notification
            chrome.notifications.create({
                type: 'basic',
                iconUrl: 'icons/icon48.png',
                title: 'Phishing Attempt Blocked!',
                message: `Risk Score: ${data.score}/100. Reason: ${data.reason}`,
                priority: 2
            });

            // Block the navigation by redirecting the user back
            chrome.tabs.goBack(details.tabId);
        }

    } catch (error) {
        console.error("LinkSentry AI Error:", error);
        // If the backend fails, show a warning icon
        chrome.action.setIcon({ path: 'icons/icon-warning.png', tabId: details.tabId });
    }
});

// Reset icon when a new tab is activated
chrome.tabs.onActivated.addListener(activeInfo => {
    chrome.action.setIcon({ path: 'icons/icon48.png', tabId: activeInfo.tabId });
});