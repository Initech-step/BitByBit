
            
<template>
<main>

    <div class="container">
        <div class="row justify-content-center align-content-center">
            <div class="col-6 col-lg-6 col-sm-8">

                <form class="form-signin" @submit.prevent="Search">
                    <div class="text-center mb-4">
                        <h1 class="h3 mb-3 font-weight-normal">Search for a suitable group to subscribe to</h1>
                        <p>You can filter your search by school, department, group name</p>
                    </div>

                    <label for="filterBy">filter by</label>
                    <select class="form-select" aria-label="Default select example" id="filterBy" required v-model="search_axis">
                        <option>----</option>
                        <option value="group_department">Department</option>
                        <option value="group_school">Group school</option>
                        <option value="group_name">Group name</option>
                    </select>
                    
                    <label for="searchText">Seach text</label>
                    <div class="form-label-group">
                        <input type="text" id="searchText" class="form-control" required v-model="search_text">
                    </div>

                    <button class="btn btn-lg btn-primary text-white btn-block w-100 mt-2" type="submit">Search</button>
                </form>
            </div> 
        </div>
        <!---groups-->
    </div>
    <br/>
    <h3 class="text-center">Results</h3>

    <div class="container">
        <div class="row">
            <div class="col-sm-6" v-for="group in groups" :key="group.id">
                <GroupCard :group_name="group.group_name" :group_school="group.group_school" :group_department="group.group_department" :id="group.id"></GroupCard>
            </div>
        </div>
    </div>

</main>
</template>

<script>
import GroupCard from '@/components/group_view_component.vue'

export default{
    name: 'Search',
    data: function(){
        return {
            search_text:"",
            search_axis:"",
            groups: ""
        }
    },
    components: {
        GroupCard
    },
    methods:{
        Search(){

            console.log("ready to search")
            console.log(this.search_axis, this.search_text)

            fetch(`http://127.0.0.1:8000/creator_apis/search_group/?axis=${this.search_axis}&search_text=${this.search_text}`)
            .then(function(response){
                return response.json()
            })
            .then(data => {
                console.log(data)
                this.groups = data
            })            
            .catch(function(){
                alert('something went wrong')
            })

        }
    }
}
    
</script>