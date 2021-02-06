<template>
    <div id="app-wrapper">
        <MainNav />
        <div class="router-wrapper">
            <router-view />
        </div>
        <MainFooter />
    </div>
</template>
<script>
import MainNav from "./components/MainNav";
import MainFooter from "./components/MainFooter";
export default {
    name: "App",
    components: { MainNav, MainFooter }
};
</script>
