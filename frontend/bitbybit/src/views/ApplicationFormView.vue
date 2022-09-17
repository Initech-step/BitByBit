<template>
    <div v-if="is_auth">
        <AdminNavbar/>
        <div class="container">
            <div class="row justify-content-center align-content-center">
                <div class="col-6 col-lg-6 col-sm-8">

                    <form class="form-signin" @submit.prevent="applyForAdmin">
                        <div class="text-center mb-4">
                            <h1 class="h3 mb-3 font-weight-bold">Apply to group</h1>
                            <p class="font-weight-bold text-info">If accepted by the admin, you will recieve a mail</p>
                        </div>

                        <label for="message">Application message</label>
                        <div class="form-label-group">
                            <textarea type="text" id="message" class="form-control" placeholder="Your application message" required v-model="application_message"></textarea>
                        </div>

                        <button class="btn btn-lg btn-primary text-white btn-block w-100 mt-2" type="submit">Apply to group</button>
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
    name: 'ApplicationFormView',
    components: {
        AdminNavbar
    },
    data(){
        return{
            application_message:"",
            is_auth:false,
            token_key:""
        }
    },
    methods:{
        applyForAdmin(){
            fetch(`http://127.0.0.1:8000/creator_apis/apply_for_admin/`, 
            {
                method:'POST',
                headers: {
                    Authorization: `Token ${this.token_key}`, 
                    'Accept': 'application/json',
                    'Content-Type':'application/json',
                },
                body:JSON.stringify({
                    application_message: this.application_message,
                    b3_group: this.$route.params.g_id
                })
            })
            .then(response => {
                console.log(response)
                alert(`You application is delivered, you will get mail if accepted`)
            })
            .catch(err => {
                alert("something went wrong")
                console.log(err)
            })
        }
    },
    mounted(){
        const toke_key = localStorage.getItem('token')
        if(toke_key){
            this.is_auth = true
            this.token_key = toke_key
        }else{
            alert('you should be redirected')
        }

    }

}
</script>

<style>

</style>