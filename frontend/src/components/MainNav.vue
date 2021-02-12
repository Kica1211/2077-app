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
            <router-link :to="{ path: `/logIn` }" v-if="!state.loggedIn">
                <div class="single-link">
                    Log in
                </div>
            </router-link>
            <router-link :to="{ path: `/userProfile` }" v-else>
                <div class="single-link">
                    Profile
                </div>
            </router-link>
            <router-link :to="{ path: `/signUp` }" v-if="!state.loggedIn">
                <div class="single-link">
                    Sign up
                </div>
            </router-link>
            <router-link :to="{ path: '/logout' }" v-else>
                <div class="single-link">
                    Logout
                </div>
            </router-link>
        </div>
    </nav>
</template>
<script>
import { reactive, onBeforeMount } from "vue";
import { useStore } from "vuex";
export default {
    name: "MainNav",
    setup() {
        const store = useStore();
        const state = reactive({
            loggedIn: true
        });
        async function checkLoggedIn() {
            state.loggedIn = await store.dispatch("auth_module/deepAuthentication");
        }
        onBeforeMount(() => {
            checkLoggedIn();
        });
        return {
            state
        };
    }
};
</script>
