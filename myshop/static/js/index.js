var b_image = document.getElementById("big_image");

document.getElementById("small_image_1").addEventListener("click", function handleClick(event){
    var image_link = event.target.getAttribute('src')
    b_image.setAttribute('src', image_link)
    
})

document.getElementById("small_image_2").addEventListener("click", function handleClick(event){
    var image_link = event.target.getAttribute('src')
    b_image.setAttribute('src', image_link)
    
})

document.getElementById("small_image_3").addEventListener("click", function handleClick(event){
    var image_link = event.target.getAttribute('src')
    b_image.setAttribute('src', image_link)
    
})