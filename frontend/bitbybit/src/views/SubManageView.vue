<template>
    <div v-if="is_auth">
        <AdminNavbar/>
        <div v-for="group in groups" :key="group.id" class="mb-3">
            <SubManageComponent :group_name="group.group_name" :group_department="group.group_department" :group_school="group.group_school" :id="group.id"></SubManageComponent>
        </div>
    </div>
    <div v-else>
        <h1>Forbiden, not logged in</h1>
    </div>
</template>

<script>
import AdminNavbar from '@/components/admin_navbar_component.vue'
import SubManageComponent from '@/components/group_sub_component.vue'
export default {
    name: 'SubManageView',
    components: {
        AdminNavbar,
        SubManageComponent
    },
    data(){
        return{
            token_key:"",
            is_auth:false,
            groups:""
        }
    },
    mounted(){
        const toke_key = localStorage.getItem('token')
        if(toke_key){
            this.token_key = toke_key
            this.is_auth = true

            fetch(`http://127.0.0.1:8000/creator_apis/view_my_managed_groups/`, 
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
                this.groups = data.group_sub_admins
            })
            .catch(err => {
                alert("something went wrong")
                console.log(err)
            })

        }else{
            alert('you should be redirected')
        }
    }
}
</script>

<style>

</style>