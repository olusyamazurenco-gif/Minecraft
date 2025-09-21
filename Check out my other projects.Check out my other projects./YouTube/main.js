console.log("MyTube Clone loaded.");

document.querySelectorAll('.like').forEach(btn=>{
    btn.onclick=()=>alert('Liked video!');
});

document.querySelectorAll('.dislike').forEach(btn=>{
    btn.onclick=()=>alert('Disliked video!');
});

document.querySelectorAll('.watch').forEach(btn=>{
    btn.onclick=()=>alert('Opening video modal...');
})
