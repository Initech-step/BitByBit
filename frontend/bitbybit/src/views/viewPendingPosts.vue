<template>
    <div v-if="is_auth">
        <AdminNavbar/>
        <div class="container">
            <div class="row justify-content-center align-content-center">
                <div class="col-8 col-lg-8 col-sm-8" v-for="post in posts" :key="post.id">
                    <PendingPostCard 
                        :title="post.letter_title" 
                        :body="post.body" 
                        :id="post.id" 
                        :writter_fname="post.written_by.first_name" 
                        :writter_lname="post.written_by.last_name" 
                        :writter_dept="post.written_by.department" 
                        :writter_school="post.written_by.school"
                        :writter_id="post.written_by.id">
                    </PendingPostCard>
                </div> 
            </div>
            <!---groups-->
        </div>
    </div>
    <div v-else>
        <h1>Forbiden, not logged in</h1>
    </div>
</template>

<script>
import AdminNavbar from '@/components/admin_navbar_component.vue'
import PendingPostCard from '@/components/PendingPostComponent.vue'

export default {
    name: 'viewPendingPostsView',
    components: {
        AdminNavbar,
        PendingPostCard
    },
    data(){
        return{
            posts:"",
            is_auth: false,
            token_key:""
        }
    },
    mounted(){

        const toke_key = localStorage.getItem('token')
        if(toke_key){
            this.is_auth = true
            this.token_key = toke_key

            // fetch posts
            fetch('http://127.0.0.1:8000/creator_apis/view_all_pending_posts_for_group/', {headers: {Authorization: `Token ${toke_key}`}})
            .then(response => {
                return response.json()
            })
            .then(data => {
                console.log(data)
                this.posts = data
                
            })
            .catch(err => {
                alert("something went really wrong")
            })

        }else{
            alert('you should be redirected')
        }

    }
}
</script>

<style>

</style>