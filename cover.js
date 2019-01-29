var ref = document.referrer;
if (ref.length > 0) {
    document.getElementById('cover').hidden = true; 
    document.getElementById('body').style.overflow = 'visible'; 
}
console.log(ref);