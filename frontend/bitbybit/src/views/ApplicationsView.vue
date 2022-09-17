<template>
    <div v-if="is_auth">
        <AdminNavbar/>
        <div class="container">
            <h3 class="text-center">Applications to my group</h3>
            <div class="row justify-content-center align-content-center">

                <div class="col-10 col-lg-10 col-sm-10" v-for="application in applications" :key="application.id">
                    <AdminApplicationCard :id="application.id" 
                                            :message="application.application_message"
                                            :b3_group="application.b3_group"
                                            :applicant="application.applicant"
                                            :token="token_key"></AdminApplicationCard>
                </div> 

            </div>
        </div>
    </div>
    <div v-else>
        <h1>Forbiden, not logged in.</h1>
    </div>
</template>

<script>
import AdminNavbar from '@/components/admin_navbar_component.vue'
import AdminApplicationCard from '@/components/admin_application_box.vue'


export default {
    name: 'ApplicationsView',
    components: {
        AdminNavbar,
        AdminApplicationCard
    },
    data(){
        return {
            is_auth:false,
            applications:"",
            token_key:""
        }
    },
    methods:{

    },

    mounted(){

        this.token_key = localStorage.getItem('token')
        if (this.token_key){
            console.log(this.token_key)
            this.is_auth = true

            fetch('http://127.0.0.1:8000/creator_apis/view_applications/', {
                headers: {
                    Authorization: `Token ${this.token_key}`, 
                }
            })
            .then(response => {
                return response.json()
            })
            .then(data => {
                // narrow the data down to the groups
                this.applications = data
            })
            .catch(err => {
                alert("something went wrong")
                console.log(err)
            })

        }else{
            alert('you are not authorized')
        }

    }
}
</script>

<style>

</style>