<template>
    <div v-if="is_auth">

        <AdminNavbar/>
        <div class="container">
            <div class="row justify-content-center align-content-center">
                <div class="col-6 col-lg-6 col-sm-8">

                    <form class="form-signin" @submit.prevent="createGroup">
                        <div class="text-center mb-4">
                            <h1 class="h3 mb-3 font-weight-normal">Create Group</h1>
                            <p>After successfull creation, set it as currently managing.</p>
                        </div>
                        
                        <label for="groupName">Group name</label>
                        <div class="form-label-group">
                            <input type="text" id="groupName" class="form-control" placeholder="Group name" required v-model="group_name">
                        </div>

                        <label for="groupDescription">Group description</label>
                        <div class="form-label-group">
                            <textarea type="text" id="groupDescription" class="form-control" placeholder="Describe your group" required v-model="group_description"></textarea>
                        </div>

                        <label for="groupSchool">Group school</label>
                        <div class="form-label-group">
                            <input type="text" id="groupSchool" class="form-control" placeholder="The group university" required v-model="group_school">
                        </div>

                        <label for="groupDepartment">Group department</label>
                        <div class="form-label-group">
                            <input type="text" id="groupDepartment" class="form-control" placeholder="The groups department" required v-model="group_department">
                        </div>

                        <button class="btn btn-lg btn-primary text-white btn-block w-100 mt-2" type="submit">Create group</button>
                    </form>

                </div> 
            </div>
            <!---groups-->
        </div>
    </div>
    <div v-else>
        <h1>Forbiden, you are not logged in</h1>
    </div>
</template>

<script>
import AdminNavbar from '@/components/admin_navbar_component.vue'
export default {
    name: 'CreateGroupView',
    components: {
        AdminNavbar
    },
    data(){
        return {
            group_name:"",
            group_description:"",
            group_school:"",
            group_department:"",
            is_auth:false,
            token_key:""

        }
    },
    methods:{
        createGroup(){
            fetch('http://127.0.0.1:8000/creator_apis/group/', 
            {
                method:'POST',
                headers: {
                    Authorization: `Token ${this.token_key}`, 
                    'Accept': 'application/json',
                    'Content-Type':'application/json',
                },
                body:JSON.stringify({
                    group_name: this.group_name,
                    group_department: this.group_department,
                    group_school: this.group_school,
                    group_description: this.group_description
                })
            })
            .then(response => {
                return response.json()
            })
            .then(data => {
                console.log(data)
                alert('group successfully created, set a currently managing')
            })
            .catch(err => {
                alert("something went wrong")
                console.log(err)
            })
        }
    },
    mounted(){
        this.token_key = localStorage.getItem('token')
        if (this.token_key){
            this.is_auth = true
            console.log(this.token_key)
        }else{
            alert('you are not authorized')
        }
    }
}
</script>

<style>

</style>