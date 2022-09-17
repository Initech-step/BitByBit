<template>
<div class="px-4 py-2 my-5 text-center">
    <img class="d-block mx-auto mb-4" src="@/assets/b3logo.png" alt="LOGO" width="80" height="75">
    <h1 class="display-5 fw-bold">BitByBit</h1>
    <div class="col-lg-6 mx-auto">
        <p class="lead mb-4">Our sole purpose is to help you read while on strike by giving you easily digestible
            content daily through emails. It takes as little as 30 mins to learn. Find and subscribe to a group today !</p>
        <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">

            <router-link :to="{name: 'search'}">
                <button type="button" class="btn btn-primary btn-lg px-4 gap-3">Find a group</button>
            </router-link>

            <router-link :to="{name: 'signup'}">
                <button type="button" class="btn btn-outline-secondary btn-lg px-4">Sign Up</button>
            </router-link>

        </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'BannerComponent'
}
</script>

<style scoped>
.bi {
fill: currentColor;
}

</style>