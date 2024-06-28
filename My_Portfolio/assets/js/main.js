/*=============== Active Link =============== */
const linkWork = document.querySelectorAll('.category__btn');
function activeWork() {
    linkWork.forEach((a) => a.classList.remove('active-work'))
    this.classList.add('active-work');
}

linkWork.forEach((a) => a.addEventListener('click', activeWork));

/*=============== Mixitup Filter =============== */
let mixerProjects = mixitup('.projects__container', {
    selectors: {
        target: '.project__item',
    },
    animation: {
        duration: 300
    },
});

/*=============== Testimonials Swiper =============== */

var testiSwiper = new Swiper('.testimonial__container', {
    loop: true,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    pagination: {
        el: '.swiper-pagination',
    },
    mousewheel : true,
    keyboard : true,
})


/*=============== Contact Form =============== */
const contactForm = document.getElementById('contact-form'),
contactName = document.getElementById('contact-name'),
contactEmail = document.getElementById('contact-email'),
Message = document.getElementById('message'),
contactMessage = document.getElementById(contact-message);

const sendEmail = (e) => {
    e.preventDefault();

    // check if the field has a value
    if (contactName.value === '' || 
        contactEmail.value === '' || 
        Message.value === '') {
            // add and remove color
            contactMessage.classList.remove('color-light');
            contactMessage.classList.add('color-dark');

            // show message
            contactMessage.textContent = 'write all the input fields';
        } else {
            // serviceId -templateId - #form - publickey
            emailjs.sendForm('service_paca217','template_tiocjpn','#contact-form','vxDcl4UI2jb0QBn6f')

            .then(() => {
                // show message and add color, window + dot to open emoji
                contactMessage.classList.add('color-light');
                contactMessage.textContent = 'Message sent';

                // remove message after 5 seconds
                setTimeout(() => {
                    contactMessage.textContent = ' ';
                }, 5000);
            } (error) => {alert(message?: any): void
                alert('OOPs! SOMETHING WENT WRONG...', error)
            }
        );

        // clear input fields

        contactName.value = '';
        
        };

       
};

contactForm.addEventListener('submit',sendEmail)

