<template>
    <v-app class="grey lighten-4">
        <Navbar class='hidden-md-and-down'/>
        <v-step-progress
          :steps="['CDT', 'MMSE', 'CVDT', 'Results']"
          passive-color="#b5b5b5"
          active-color="#23d160"
          :passive-thickness="5"
          :active-thickness="5"
          :line-thickness="5"
          :current-step="step"
          icon-class="mdi-check"/>

        <!-- Transitions for my views -->
        <transition :name="'slider-' + anim_dir" mode='out-in'>
            <router-view class = 'mx-4 mb-4'/>
        </transition>

    </v-app>
</template>



<script lang="ts">
import Vue from "vue";
import Navbar from "@/components/Navbar.vue";
import StepProgress from "vue-step-progress";
import 'vue-step-progress/dist/main.css';

// Setting Website Name
document.title = "ISAD";

// Route to Steps
const steps: string[] = [
    "Dashboard",
    "Projects", 
    "Team", 
];

export default Vue.extend({
    name: "App",
    components: {Navbar, "v-step-progress": StepProgress},
    data: () => ({
        step: 0,
        anim_dir: "right"
    }),

    watch: { // Observer for route changes

        $route (to, from){ // Changes Progress bar accordingly
            console.log(to);
            console.log(from);

            // What is the next index position
            var next: number = steps.indexOf(to.name);

            // Handles Animation Slide Direction
            if (next < this.step) this.anim_dir = "left";
            else this.anim_dir = "right";

            // Finally sets the current index
            this.step = next;
        }
    }
});
</script>



<!-- Slide left & right animations -->
<style>
.slider-right-enter {
  opacity: 0;
  transform: translatex(100%);
}

.slider-right-enter-to {
  opacity: 1;
  transition: all 0.5s ease-out;
}

.slider-right-leave-to {
  opacity: 0;
  transform: translatex(-100%);
  transition: all 0.5s ease-out;
}

.slider-left-enter {
  opacity: 0;
  transform: translatex(-100%);
}

.slider-left-enter-to {
  opacity: 1;
  transition: all 0.5s ease-out;
}

.slider-left-leave-to {
  opacity: 0;
  transform: translatex(100%);
  transition: all 0.5s ease-out;
}
</style>
