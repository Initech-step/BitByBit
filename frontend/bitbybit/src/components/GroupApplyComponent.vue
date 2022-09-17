<template>
    <div class="card mb-2">
        <div class="card-body">
          <h5 class="card-title">Group name: <span> {{ group_name }}</span></h5>
          <p class="card-text">Group department: {{ group_department }}</p>
          <p class="card-text">Group school: {{ group_school }}</p>

          <div class="d-flex flex-row">
            
              <button class="btn btn-primary btn-md" @click="groupDetailPage(id)">Details</button>
              <button class="btn btn-success btn-md mx-2" @click="applyToGroup(id)">Apply</button>

          </div>
          
        </div>
      </div>
  </template>
  
  <script>
  export default {
      name: 'ApplyToGroupCard',
      props: ['group_name', 'group_department', 'group_school', 'id'],
      methods:{
        groupDetailPage(id){
          this.$router.push({name:'group_details', params:{g_id:id}})
        },
        applyToGroup(id){
          this.$router.push({name:'apply_to_group', params:{g_id:id}})
        }
      }
  }
  </script>
  
  <style>
  
  </style>