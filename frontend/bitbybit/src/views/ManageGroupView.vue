<template>
    <div v-if="is_auth">
        <div v-if="has_currently_managing">
            <AdminNavbar/>
            <div class="container">
                <div class="row">
                    <div class="col-8 col-lg-8 col-sm-8">
                        <!---State for application-->
                        <form class="form-signin" @submit.prevent="submitApprovalState">
                            <div class="mb-4">
                                <h5 class="h3 font-weight-normal">Application state for group manager</h5>
                            </div>

                            <label for="filterBy">Choose state</label>
                            <select class="form-select" aria-label="Default select example" id="filterBy" required v-model="approval_state">
                                <option selected>----</option>
                                <option value="on">Open application</option>
                                <option value="off">Close application</option>
                            </select>

                            <button class="btn btn-lg btn-primary text-white mt-2" type="submit">Save</button>
                        </form>


                        <br/>
                        <hr/>
                        <!---Set message for new subscribers-->
                        <form class="form-signin" @submit.prevent="setMessageForSubscriber">
                            <div class="mb-4">
                                <h5 class="h3 font-weight-normal">Set message for new subscribers</h5>
                                <p class="text-info">If not set, it will resolve to default</p>
                            </div>

                            <label for="newSubscriber">Message for new subscribers</label>
                            <div class="form-label-group">
                                <textarea type="text" id="newSubscriber" class="form-control" required v-model="messageForSubscriber"></textarea>
                            </div>

                            <button class="btn btn-lg btn-primary text-white mt-2" type="submit">Save</button>
                        </form>
                        

                        <br/>
                        <hr/>
                        <!---Set message for new admins-->
                        <form class="form-signin" @submit.prevent="setMessageForAdmin">
                            <div class="mb-4">
                                <h5 class="h3 font-weight-normal">Set message for new admins</h5>
                                <p class="text-info">If not set, it will resolve to default</p>
                            </div>

                            <label for="newAdmin">Message for new Admins</label>
                            <div class="form-label-group">
                                <textarea type="text" id="newAdmin" class="form-control" required v-model="messageForAdmin"></textarea>
                            </div>

                            <button class="btn btn-lg btn-primary text-white mt-2" type="submit">Save</button>
                        </form>
                    </div> 
                </div>
            </div>


            <br/>
            <hr/>
            <!---Manage admins-->
            <div class="container">
                <button @click="loadSubAdmins" class="btn btn-lg btn-info m-2">load admins</button>
                <div class="row">
                    <br/>
                    <h5>Manage Admins</h5>

                    <div class="col-8 col-lg-8 col-sm-8" v-for="admin in sub_admins" :key="admin.id">
                        <div class="card mb-3">
                            <div class="card-body">
                                <h5 class="card-title">Admin name: {{ admin.first_name }}</h5>
                                <p class="card-text">last name: {{ admin.last_name }}</p>
                                <p class="card-text">Admin department:{{ admin.department }}</p>
                                <p class="card-text">Admin school: {{ admin.school }}</p>
                                <p class="card-text">Admin school: {{ admin.set_year }}</p>
                                <div class="d-flex flex-row">
                                    <button class="btn btn-danger" @click="expelAdmin(admin.id)">Expel admin</button>
                                </div>
                            </div>
                        </div>
                    </div> 

                </div>
            </div>

        </div>
        <div v-else>
            <h1>You do not have a currently managing</h1>
        </div>

    </div>
    <div v-else>
        <h1>Forbiden, you are not logged in</h1>
    </div>

</template>





<script>
import AdminNavbar from '@/components/admin_navbar_component.vue' 
export default {
    name: 'ManageGroupView',
    components: {
        AdminNavbar
    },
    data(){
        return {
            messageForSubscriber:"",
            messageForAdmin:"",
            approval_state:"",
            is_auth:false,
            has_currently_managing:"",
            token_key:"",
            sub_admins:""
        }
    },
    methods: {
        
        setMessageForSubscriber(){
            fetch('http://127.0.0.1:8000/creator_apis/set_new_subcriber_email/', 
            {
                method:'POST',
                headers: {
                    Authorization: `Token ${this.token_key}`, 
                    'Accept': 'application/json',
                    'Content-Type':'application/json',
                },
                body:JSON.stringify({
                    message: this.messageForSubscriber,
                })
            })
            .then(response => {
                console.log(response)
                alert(`Your message has been set`)
            })
            .catch(err => {
                alert("something went wrong")
                console.log(err)
            })
        },

        setMessageForAdmin(){
            fetch('http://127.0.0.1:8000/creator_apis/set_new_sub_admin_email/', 
            {
                method:'POST',
                headers: {
                    Authorization: `Token ${this.token_key}`, 
                    'Accept': 'application/json',
                    'Content-Type':'application/json',
                },
                body:JSON.stringify({
                    message: this.messageForAdmin
                })
            })
            .then(response => {
                console.log(response)
                alert(`Your message has been set`)
            })
            .catch(err => {
                alert("something went wrong")
                console.log(err)
            })
        },

        submitApprovalState(){
            fetch('http://127.0.0.1:8000/creator_apis/toggle_application/', 
            {
                method:'PUT',
                headers: {
                    Authorization: `Token ${this.token_key}`, 
                    'Accept': 'application/json',
                    'Content-Type':'application/json',
                },
                body:JSON.stringify({
                    state: this.approval_state,
                })
            })
            .then(response => {
                return response.json()
            })
            .then(data => {
                console.log(data)
                alert(`Your group application state is ${data.admission_state}`)
            })
            .catch(err => {
                alert("something went wrong")
                console.log(err)
            })

        },

        loadSubAdmins(){
            fetch('http://127.0.0.1:8000/creator_apis/view_my_sub_admins/', 
            {
                headers: {
                    Authorization: `Token ${this.token_key}`,
                }
            })
            .then(response => {
                console.log(response)
                return response.json()
            })
            .then(data => {
                console.log(data)
                this.sub_admins = data
            })
            .catch(err => {
                alert("something went wrong")
                console.log(err)
            })
        },

        expelAdmin(id){
            fetch(`http://127.0.0.1:8000/creator_apis/expel_sub_admin/${id}/`, 
            {
                method:'POST',
                headers: {
                    Authorization: `Token ${this.token_key}`, 
                    'Accept': 'application/json',
                    'Content-Type':'application/json',
                }
            })
            .then(response => {
                console.log(response)
                alert(`Admin successfully expelled`)
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
            this.token_key = toke_key
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
                }
            })
            .catch(err => {
                console.log(err)
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