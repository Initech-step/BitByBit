<template>
    <div class="card m-2">
        <div class="card-body">
          <p class="card-text">Application message: {{ message }}</p>

          <div class="d-flex flex-row">
            <button class="btn btn-sm btn-success mx-2" @click="acceptApplication(id, token)">Accept application</button>
            <button class="btn btn-sm btn-danger">Delete application</button>
          </div>
          
        </div>
      </div>
  </template>
  
<script>
export default {
    name: 'AdminApplicationCard',
    props: ['message', 'id', 'applicant', 'b3_group', 'token'],
    methods:{
      acceptApplication(id, token){
        alert(`accept ${id} with ${token}`)
        fetch('http://127.0.0.1:8000/creator_apis/view_applications/', 
        {
          method:'POST',
          headers: {
              Authorization: `Token ${token}`, 
              'Accept': 'application/json',
              'Content-Type':'application/json',
          },
          body:JSON.stringify({
              id: id,

          })
        })
        .then(response => {
            console.log(response)
            alert('Application accepted')
        })
        .catch(err => {
            alert("something went wrong")
            console.log(err)
        })

      }
    }
}
</script>