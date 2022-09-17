<template>
    <div v-if="is_auth">

        <AdminNavbar/>
        <div class="container">
            <div class="row justify-content-center align-content-center">
                <div class="col-8 col-lg-8 col-sm-10">

                    <div v-if="has_currently_managing">

                        <div class="card">
                            <div class="card-header">
                                Group you are currently managing
                            </div>
                            <div class="card-body">
                                <h5 class="card-title">Group name: {{ group_data.group_name }}</h5>
                                <p class="card-text">Group department: {{ group_data.group_department }}</p>
                                <p class="card-text">Group school: {{ group_data.group_school }}</p>
                                
                                <div class="d-flex flex-row">
                                    <button class="btn btn-primary" @click="goPost(group_data.id)">Make post</button>

                                    <button class="btn btn-warning mx-2" @click="viewPending">Review posts</button>

                                    <router-link :to="{name: 'manage_group'}">
                                        <a href="#" class="btn btn-danger">Manage group</a>
                                    </router-link>
                                </div>
                                
                            </div>
                        </div>
                    </div>

                    <div v-else>
                        <h1>You have not selected any group for currently managing</h1>
                    </div>

                </div> 
            </div>
            <!---groups-->
        </div>

    </div>
    <div v-else>
        <h1>Forbiden, not loged in.</h1>
    </div>
</template>

<script>
import AdminNavbar from '@/components/admin_navbar_component.vue'
export default {
    name: 'CurrentlyManagingView',
    components: {
        AdminNavbar
    },
    data(){
        return {
            group_data:"",
            is_auth:false,
            has_currently_managing:false
        }
    },
    methods: {
        goPost(id){
            this.$router.push({name:'make_post', params: { g_id:id }})
        },
        viewPending(){
            this.$router.push({name:'view_pending_posts'})
        }

    },
    mounted(){
        const toke_key = localStorage.getItem('token')
        if(toke_key){
            this.is_auth = true
            // fetch user data
            fetch('http://127.0.0.1:8000/creator_apis/has_managing/', {headers: {Authorization: `Token ${toke_key}`}})
            .then(response => {
                return response.json()
            })
            .then(data => {

                console.log(data)
                if(data.status === false){
                    this.has_currently_managing = false
                }else{
                    this.has_currently_managing = true
                    this.group_data = data.group_data
                }
            })
            .catch(err => {
                alert("something went wrong")
            })

        }else{
            alert('you should be redirected')
        }
    }

}
</script>

<style>

</style>