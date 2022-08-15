<template>
    <v-app class="grey lighten-4">
        <Navbar />

        <!-- Transitions for my views -->
        <transition name="slither" mode="out-in">
            <router-view class = 'mx-4 mb-4'/>
        </transition>

    </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import Navbar from "@/components/Navbar.vue";

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

<style>
.slither-enter-active, .slither-leave-active {
  transition: transform 1s;
}

.slither-enter, .slither-leave-to {
  transform: translateX(-100%);
}

.slither-enter-to, .slither-leave {
  transform: translateX(0);
}
</style>
