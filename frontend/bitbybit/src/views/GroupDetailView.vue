<template>
    <NavbarComponent/>
    <div class="container">
        <div class="row">
            <div class="col-8 col-lg-8 col-sm-8">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">Group name: <span>{{ group_data.group_name }} </span></h5>
                        <p class="card-text">Group department: {{ group_data.group_department }}</p>
                        <p class="card-text">Group school: {{ group_data.group_school }}</p>
                        <p class="card-text">Number of subscribers: {{ number_of_sub }}</p>
                    </div>
                </div>
            </div> 
        </div>
    </div>

    <br/>
    <div class="container">
        <h5 class="text-info">Subscribe to group</h5>
        <div class="row">
            <div class="col-8 col-lg-8 col-sm-8">
                <form class="form-signin" @submit.prevent="subscribeEmail">
                    <label for="subEmail">Your email</label>
                    <div class="form-label-group">
                        <input type="email" id="subEmail" class="form-control" required v-model="email_sub">
                    </div>
                    <button class="btn btn-lg btn-primary text-white mt-2" type="submit">Subscribe</button>
                </form>
            </div> 
        </div>
    </div>


    <!---See sub admins-->
    <br/>
    <hr/>
    <div class="container">
        <div class="row">
            <h5 class="text-info">Group creator</h5>

            <div class="col-12 col-lg-12 col-sm-12">
                <div class="card">
                    <div class="card-body">
                        <h6 class="card-title">Admin name: {{ groupADMIN.first_name }}</h6>
                        <p class="card-title">Last name: {{ groupADMIN.last_name }}</p>
                        <p class="card-title">Set year: {{ groupADMIN.set_year }}</p>
                        <p class="card-text">Admin department: {{ groupADMIN.department }}</p>
                        <p class="card-text">Admin school: {{ groupADMIN.school }}</p>
                    </div>
                </div>
            </div> 


        </div>
    </div>


    <!---See sub admins-->
    <br/>
    <hr/>
    <div class="container">
        <div class="row">
            <h5 class="text-info">Group admins</h5>

            <div class="col-12 col-lg-12 col-sm-12" v-for="admin in group_data.group_admins" :key="admin.id">
                <div class="card">
                    <div class="card-body">
                        <h6 class="card-title">Admin name: {{ admin.first_name }}</h6>
                        <p class="card-title">Last name: {{ admin.last_name }}</p>
                        <p class="card-title">Set year: {{ admin.set_year }}</p>
                        <p class="card-text">Admin department: {{ admin.department }}</p>
                        <p class="card-text">Admin school: {{ admin.school }}</p>
                    </div>
                </div>
            </div> 

        </div>
    </div>
</template>

<script>
import NavbarComponent from '@/components/navbar.vue'
export default {
    name: 'GroupDetailView',
    data(){
        return {
            group_data: "",
            groupADMIN:"",
            number_of_sub:"",
            email_sub:""
        }
    },
    components: {
        NavbarComponent
    },
    methods:{
        subscribeEmail(){

            fetch('http://127.0.0.1:8000/creator_apis/subscribe/', 
            {
                method:'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type':'application/json',
                },
                body:JSON.stringify({
                    email: this.email_sub,
                    b3_group: this.$route.params.g_id,
                })
            })
            .then(response => {
                alert('You have successfully subscribed, you will get mail')
            })
            .catch(err => {
                alert("something went wrong")
                console.log(err)
            })

        }
    },
    mounted(){
        if (this.$route.params.g_id){

            let Gid = this.$route.params.g_id
            fetch(`http://127.0.0.1:8000/creator_apis/view_group_detail/${Gid}/`)
            .then(function(response){
                return response.json()
            })
            .then(data => {
                this.group_data = data
                this.groupADMIN = data.group_creator
                this.number_of_sub = data.subscribers.length
            })            
            .catch(function(){
                alert('something went wrong')
            })

        }else{
            alert("Route configured wrongly")
        }
    }
}
</script>

<style>

</style>