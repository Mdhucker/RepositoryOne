document.addEventListener("DOMContentLoaded", function() {
    var userAgent = navigator.userAgent || navigator.vendor || window.opera;
    var whatsappLink = document.getElementById('whatsapp-link');
    var phoneNumber = '+255625207028';  // Your phone number

    if (/android/i.test(userAgent)) {
        // If the device is Android, use WhatsApp app link
        whatsappLink.href = 'whatsapp://send?phone=' + phoneNumber;
    } else if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
        // If the device is iOS, use WhatsApp app link
        whatsappLink.href = 'whatsapp://send?phone=' + phoneNumber;
    } else {
        // For other devices, use WhatsApp web link
        whatsappLink.href = 'https://web.whatsapp.com/send?phone=' + phoneNumber;
    }
});
