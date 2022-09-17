<template>
  <div class="card">
      <div class="card-body">
        <h5 class="card-title">Group name: <span> {{ group_name }}</span></h5>
        <p class="card-text">Group department: {{ group_department }}</p>
        <p class="card-text">Group school: {{ group_school }}</p>
        <button class="btn btn-primary" @click="viewGroupDetail(id)">Details</button>
      </div>
    </div>
</template>

<script>
export default {
    name: 'GroupCard',
    props: ['group_name', 'group_department', 'group_school', 'id'],
    methods: {
      viewGroupDetail: function(id){
        this.$router.push({name:'group_details', params:{g_id:id}})
      },
    }
}
</script>

<style>

</style>