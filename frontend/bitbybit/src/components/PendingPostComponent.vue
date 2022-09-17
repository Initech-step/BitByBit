<template>
    <div class="card mb-2">
        <div class="card-body">
          <h5 class="card-title">post title: <span> {{ title }}</span></h5>
          <p class="card-text">post body: {{ body }}</p>
          <p class="card-text">writter first name: {{ writter_fname }}</p>
          <p class="card-text">writter last name: {{ writter_lname }}</p>
          <p class="card-text">writter department: {{ writter_dept }}</p>
          <p class="card-text">writter university: {{ writter_school }}</p>

          <div class="d-flex flex-row">
              <button class="btn btn-success btn-md" @click="ApprovePost(id)">Approve post</button>
          </div>
          
        </div>
      </div>
  </template>
  
  <script>
  export default {
      name: 'PendingPostCard',
      props: ['writter_fname', 'writter_lname', 'writter_dept', 'writter_school', 'writter_id', 'id', 'title', 'body'],
      data(){
        return{
            token_key:localStorage.getItem('token')
        }
      },
      methods:{
        ApprovePost(id){

            fetch(`http://127.0.0.1:8000/creator_apis/approve_post/${id}/`, 
            {
                method: 'PUT',
                headers: {
                    Authorization: `Token ${this.token_key}`
                }
            })
            .then(response => {
                return response.json()
            })
            .then(data => {
                console.log(data)
                alert('Post has been approved, mails on the way')
            })
            .catch(err => {
                alert("something went wrong")
                console.log(err)
            })
        }
      }
  }
  </script>
  
  <style>
  
  </style>