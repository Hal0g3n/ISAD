<template>
    <v-app class="grey lighten-4">
        <Navbar />

        <v-main>
        <router-view class="mx-4 mb-4"/>
        </v-main>
    </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import Navbar from "@/components/Navbar.vue"

// Setting Website Name
document.title = "ISAD";

export default Vue.extend({
    name: "App",
    components: {Navbar},
    data: () => ({
        //
    }),
});
</script>
