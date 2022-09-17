<template>
    <div class="container">
        <div class="row justify-content-center align-content-center">
            <div class="col-8 col-lg-8 col-sm-10">

                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Group name: {{ group_name }}</h5>
                        <p class="card-text">Group department: {{ group_department }}</p>
                        <p class="card-text">Group school: {{ group_school }}</p>
                        
                        <div class="d-flex flex-row">
                            
                            <button class="btn btn-primary" @click="goPost(id)">Make post</button>
                        </div>
                        
                    </div>
                </div>

            </div> 
        </div>
        <!---groups-->
    </div>
</template>

<script>
export default {
    name: 'SubManageComponent',
    props: ['group_name', 'id', 'group_department', 'group_school'],
    methods: {
        goPost(id){
            this.$router.push({name:'make_post', params: { g_id:id }})
        }
    }
}
</script>

<style>

</style>