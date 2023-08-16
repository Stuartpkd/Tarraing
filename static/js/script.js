let savedArtworkBtn = document.getElementById("artwork-btn"); // button to toggle saved artworks

let postsBtn = document.getElementById("post-btn"); // button to toggle to see posts instead

let posts = document.getElementById("post-list"); // to show the posts

let savedArtworks = document.getElementById("saved-artwork-list"); // to show the artworks

savedArtworkBtn.addEventListener("click", displayArtworks);
postsBtn.addEventListener("click", displayPosts);

function displayArtworks() {
    console.log("artworks")
    savedArtworks.classList.remove("hide");
    posts.classList.add("hide");
}

function displayPosts() {
    console.log("posts")
    savedArtworks.classList.add("hide");
    posts.classList.remove("hide");
}