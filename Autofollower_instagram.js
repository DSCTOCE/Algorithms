//  Javascript code to follow people automatically //


(() => {
    let i = 0;
    const followInterval = setInterval(() => {
        if (i >= 30) {
            clearInterval(followInterval);
            return;
        }
        const buttons = document.querySelectorAll('button');
        const nextButton = buttons[i];
        nextButton.click();
        i += 1;
    }, 500)
})()


// If these worked , then enjoy //
