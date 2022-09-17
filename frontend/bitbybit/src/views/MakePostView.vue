<template>
    <div v-if="is_auth">
        <AdminNavbar/>
        <div class="container">
            <div class="row justify-content-center align-content-center">
                <div class="col-6 col-lg-6 col-sm-8">
                    <form class="form-signin" @submit.prevent="makePost">
                        <div class="text-center mb-4">
                            <h1 class="h3 mb-3 font-weight-normal">Make post</h1>
                        </div>
                        
                        <label for="postTitle">Post title</label>
                        <div class="form-label-group">
                            <input type="text" id="postTitle" class="form-control" required v-model="post_title">
                        </div>

                        <label for="postBody">body</label>
                        <div class="form-label-group">
                            <textarea type="text" id="postBody" class="form-control" required v-model="post_body"></textarea>
                        </div>

                        <button class="btn btn-lg btn-primary text-white btn-block w-100 mt-2" type="submit">Make Post</button>
                    </form>
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

export default {
    name: 'MakePostView',
    components: {
        AdminNavbar
    },
    data(){
        return{
            is_auth: false,
            token_key:"",
            post_title:"",
            post_body:""

        }
    },
    mounted(){
        const toke_key = localStorage.getItem('token')
        if(toke_key){
            this.token_key = toke_key
            this.is_auth = true
        }else{
            alert('you should be redirected')
        }
    },


    methods: {
        makePost(){
            fetch(`http://127.0.0.1:8000/creator_apis/send_newsletter/${ this.$route.params.g_id}/`, 
            {
                method:'POST',
                headers: {
                    Authorization: `Token ${this.token_key}`, 
                    'Accept': 'application/json',
                    'Content-Type':'application/json',
                },
                body:JSON.stringify({
                    letter_title: this.post_title,
                    body: this.post_body
                })
            })
            .then(response => {
                console.log(response)
                alert(`Newsletters on the way, nice job!`)
            })
            .catch(err => {
                alert("something went wrong")
                console.log(err)
            })
        },
    }
}
</script>

<style>
</style>
