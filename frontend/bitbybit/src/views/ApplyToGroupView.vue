<template>
    <div v-if="is_auth">
        <AdminNavbar/>
        <div class="container">
            <div class="row justify-content-center align-content-center">
                <div class="col-8 col-lg-8 col-sm-8" v-for="group in groups" :key="group.id">
                    <ApplyToGroupCard :group_name="group.group_name" :group_department="group.group_department" :id="group.id" :group_school="group.group_school"/>
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
import ApplyToGroupCard from '@/components/GroupApplyComponent.vue'

export default {
    name: 'ApplicationsToGroupView',
    components: {
        AdminNavbar,
        ApplyToGroupCard
    },
    data(){
        return{
            groups:"",
            is_auth: false
        }
    },
    mounted(){

        const toke_key = localStorage.getItem('token')
        if(toke_key){
            this.is_auth = true
            // fetch user data
            fetch('http://127.0.0.1:8000/creator_apis/view_group_open_for_apply/', {headers: {Authorization: `Token ${toke_key}`}})
            .then(response => {
                return response.json()
            })
            .then(data => {
                console.log(data)
                this.groups = data
                
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