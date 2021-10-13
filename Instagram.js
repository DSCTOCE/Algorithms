// javaScript to like Instagram post Automatically 

let likesGiven = 0;
setInterval(() => {
	let   heart = document.querySelector('button.wpO6b'),
        arrow = document.querySelector('.coreSpriteRightPaginationArrow');
	if (heart) {
		
		likesGiven++;
    heart.click();
    }
	arrow.click();
	console.log(`You've liked ${likesGiven} post(s)!`);
}, 2000);
