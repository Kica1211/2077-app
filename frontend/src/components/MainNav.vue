<template>
    <nav class="main-nav">
        <div class="cyber-logo">
            <img src="/img/main_logo1.png" alt="" />
        </div>
        <!-- <div class="cutted"></div> -->
        <div class="nav-links">
            <router-link :to="{ path: `/` }">
                <div class="single-link">
                    News
                </div>
            </router-link>
            <router-link :to="{ path: `/gallery` }">
                <div class="single-link">
                    Gallery
                </div>
            </router-link>
            <router-link :to="{ path: `/logIn` }">
                <div class="single-link">
                    Log in
                </div>
            </router-link>
            <router-link :to="{ path: `/signUp` }">
                <div class="single-link">
                    Sign up
                </div>
            </router-link>
        </div>
    </nav>
</template>
<script>
export default {
    name: "MainNav"
};
</script>
