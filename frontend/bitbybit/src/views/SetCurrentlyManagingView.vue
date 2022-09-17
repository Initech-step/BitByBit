<template>
    <div v-if="is_auth">
        <AdminNavbar/>
        <div class="container">
            <div class="row justify-content-center align-content-center">
                <div class="col-8 col-lg-8 col-sm-8">

                    <div v-for="group in ready_groups" :key="group.id">
                        <MyCreatedGroupCard :group_name="group.group_name" 
                            :group_description="group.group_description"
                            :group_department="group.group_department"
                            :group_school="group.group_school"
                            :id="group.id">
                        </MyCreatedGroupCard>
                    </div>
                    
                </div> 
            </div>
            <!---groups-->
        </div>
    </div>
    <div v-else>
        <h1>Forbiden, not loged in</h1>
    </div>
</template>

<script>
import AdminNavbar from '@/components/admin_navbar_component.vue'
import MyCreatedGroupCard from '@/components/MyCreatedGroupComponent.vue'

export default {
    name: 'SetCurrentlyManagingView',
    components: {
        AdminNavbar,
        MyCreatedGroupCard
    },
    data(){
        return {
            token_key:"",
            is_auth:false,
            ready_groups: ""
        }
    },
    mounted(){
        this.token_key = localStorage.getItem('token')
        if (this.token_key){
            console.log(this.token_key)
            this.is_auth = true

            fetch('http://127.0.0.1:8000/creator_apis/view_my_created_groups/', {
                headers: {
                    Authorization: `Token ${this.token_key}`, 
                }
            })
            .then(response => {
                return response.json()
            })
            .then(data => {
                // narrow the data down to the groups
                this.ready_groups = data.groups_created
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