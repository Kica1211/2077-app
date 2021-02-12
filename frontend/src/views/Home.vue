<template>
    <div class="home-wrapper">
        <Welcome />
        <HomeContent />
    </div>
</template>
<script>
import Welcome from "../components/home/Welcome";
import HomeContent from "../components/home/HomeContent";
import { useStore } from "vuex";

export default {
    name: "Home",
    components: { Welcome, HomeContent },
    setup() {
        const store = useStore();
        const API_ADDRESS = store.state.API_ADDRESS;
        return {
            API_ADDRESS
        };
    }
};
</script>
