<template>
    <div class="card mb-2">
        <div class="card-body">
          <p class="card-title">Group name: <span> {{ group_name }} </span></p>
          <p class="card-text">Group department: {{ group_department }}</p>
          <p class="card-text">Group school: {{ group_school }}</p>
          <p class="card-text">Group school: {{ group_description }}</p>

          <div class="d-flex flex-row">
            <button class="btn btn-primary btn-md" @click="setCurrentlyManaging(id)">Set as currently managing</button>
          </div>
          
        </div>
      </div>
  </template>
  
  <script>
  export default {
      name: 'MyCreatedGroupCard',
      props: ['group_name', 'group_department', 'group_school', 'id', 'group_description'],
      data(){
        return {
          me:"ini",
          token_key:""
        }
      }, 
      methods:{
        setCurrentlyManaging(id){
          this.token_key = localStorage.getItem('token')

          fetch(`http://127.0.0.1:8000/creator_apis/set_managing/${id}/`, {
            method: 'PUT',
            headers: {
                Authorization: `Token ${this.token_key}`, 
            }
          })
          .then(response => {
            return response.json()
          })
          .then(data => {
            console.log(data)
            alert("Successfully set as currently managing")
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