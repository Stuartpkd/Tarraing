function confirmDelete() {
    return confirm("Are you sure you want to delete this post?");
}




function closeCommentSuccessAlert() {
    const commentSuccessAlert = document.getElementById('comment-success-alert');
    commentSuccessAlert.style.display = 'none';
}


function handleCommentSubmission() {
    const commentSuccessAlert = document.getElementById('comment-success-alert');
    commentSuccessAlert.style.display = 'block';
}