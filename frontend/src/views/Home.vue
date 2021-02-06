<template>
    <div class="home-wrapper">
        <Welcome />
        <HomeContent />
    </div>
</template>
<script>
import Welcome from "../components/home/Welcome";
import HomeContent from "../components/home/HomeContent";
export default {
    name: "Home",
    components: { Welcome, HomeContent }
};
</script>
