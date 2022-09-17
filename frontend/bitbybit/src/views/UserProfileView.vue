<template>
    <div v-if="is_auth">
        <AdminNavbar/>
        <div class="container my-5">
            <div class="bg-light p-5 rounded">
                <div class="col-sm-8 py-2">
                    <h4 class="display-5 fw-normal">User Profile</h4>
                    <p class="fs-5">email: {{ user_data.email }}</p>
                    <p>first name: {{ user_data.first_name }}</p>
                    <p>last name: {{ user_data.last_name }}</p>
                    <p>department: {{ user_data.department }}</p>
                    <p>set year: {{ user_data.set_year }}</p>
                    <p>University: {{ user_data.school }}</p>
                    <a class="btn btn-primary" href="../components/navbar/#offcanvas" role="button">Your profile &raquo;</a>
                </div>
            </div>
        </div>
    </div>
    <div v-else>
        <h1>Forbiden, not logged in</h1>
    </div>
</template>

<script>
import AdminNavbar from '@/components/admin_navbar_component.vue'
export default {
    name: 'UserProfileView',
    components: {
        AdminNavbar
    },
    data(){
        return{
            is_auth:false,
            user_data:""
        }
    },
    mounted(){
        const toke_key = localStorage.getItem('token')
        if(toke_key){
            fetch('http://127.0.0.1:8000/creator_apis/view_myself/', {headers: {Authorization: `Token ${toke_key}`}})
            .then(response => {
                return response.json()
            })
            .then(data => {
                console.log(data)
                this.user_data = data
                this.is_auth = true
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