

let images = ['pic2.jpg', 'pic3.jpg', 'pic1.jpg'];
let index = 0;

function changeImage() {
    document.getElementById('slideshow-image').style.opacity = 0;
    setTimeout(() => {
        document.getElementById('slideshow-image').src= images[index];
        document.getElementById('slideshow-image').style.opacity = 1;
        index = (index +1) % images.length;
    }, 200);
    
}


setInterval(changeImage, 5000);

function myFunction() {
    window.location.href = "homePage/HomePage.html";

}

function homeFunction() {
    window.location.href = "../index.html";
}


// Modal Functions

// let slideIndex = 0;

// function openModal(imageSrc) {
    // document.getElementById('modal-image').src = imageSrc;
    // document.getElementById('modal').style.display = 'block';

    

    // // override the width image to 60
    // var modalImage = document.getElementById('modal-image');
    // modalImage.src = imageSrc;
   
    // // calculate the width of the viewport
    // var viewportWidth = window.innerWidth || document.documentElement.clientWidth;
    
    // // set the modal image to 60 viewport width
    // modalImage.style.width = (viewportWidth * 0.60) + 'px';
    // document.getElementById('modal').style.display = 'block';



//     // get and modify modal
//     var modal = document.getElementById('modal');
//     modal.style.display = 'block';

    // //Disable Scrolling
    // document.body.style.overflow = 'hidden';

//     //show the image at the correct index
//     //find the index of the current imag
   

// }

function closeModal() {
    document.getElementById('modal').style.display = 'none';
    // slideIndex = 0;

    // call modal
    var modal = document.getElementById('modal');
    modal.style.display = 'none';

    //Enable Scrolling
    document.body.style.overflow = 'auto';
    
}

function openModal(clickedImageSrc) {
    document.getElementById('modal-image').src = clickedImageSrc;
    document.getElementById('modal').style.display = 'block';

        // override the width image to 60
        var modalImage = document.getElementById('modal-image');
        modalImage.src = clickedImageSrc;
       
        // calculate the width of the viewport
        var viewportWidth = window.innerWidth || document.documentElement.clientWidth;
        
        // set the modal image to 60 viewport width
        modalImage.style.width = (viewportWidth * 0.60) + 'px';
        document.getElementById('modal').style.display = 'block';

        //Disable Scrolling
        document.body.style.overflow = 'hidden';

    //slideShow
    var images = document.querySelectorAll('.gallery img');
    var index = Array.from(images).findIndex(img => img.src == clickedImageSrc);

    document.getElementById('modal-image').src = clickedImageSrc;
    document.getElementById('modal').style.display = 'block';

    slideIndex = index;
    showSlides(slideIndex);
}

function showSlides(n) {
    var images = document.querySelectorAll('.gallery img');
    slideIndex = n;

    if (slideIndex >= images.length) {
        slideIndex = 0;
    }
    if (slideIndex < 0) {
        slideIndex = images.length - 1;
    }

    var modalImage = document.getElementById('modal-image');
    modalImage.src = images[slideIndex].src;
}

function plusSlides(n) {
    var images = document.querySelectorAll('.gallery img');
    var newIndex = slideIndex + n;

    if (newIndex >= images.length) {
        slideIndex = 3;
    } else if (newIndex < 0) {
        slideIndex = images.length + 1;
    } else {
        slideIndex = newIndex + 1;
    }

    showSlides(slideIndex)
}




