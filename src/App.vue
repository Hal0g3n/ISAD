<template>
    <v-app class="grey lighten-4">
        <Navbar class='hidden-md-and-down'/>
        <ProgressBar
            :steps="steps"
            :active-step="0"
            :is-reactive="true"
            :showBridge="true"
            :showLabel="false"
            class = 'mx-4'
            @onStepChanged="onStepChanged"/>

        <!-- Transitions for my views -->
        <transition :name="'slider-' + anim_dir" mode='out-in'>
            <router-view class = 'mx-4 mb-4'/>
        </transition>

    </v-app>
</template>



<script lang="ts">
import Vue from "vue";
import Navbar from "@/components/Navbar.vue";
import ProgressBar from "@/components/ProgressBar.vue";

// Setting Website Name
document.title = "ISAD";

// Route to Steps
const steps: string[] = [
    "",
    "Projects", 
    "Team", 
];

export default Vue.extend({
    name: "App",
    components: {Navbar, ProgressBar},
    data: () => ({
        step: 0,
        steps,
        anim_dir: "right"
    }),

    watch: { // Observer for route changes

        $route (to, from){ // Changes Progress bar accordingly

            // What is the next index position
            var next: number = steps.indexOf(to.name);

            // Handles Animation Slide Direction
            if (next < this.step) this.anim_dir = "left";
            else this.anim_dir = "right";

            // Finally sets the current index
            this.step = next;
        }
    },

    // define methods under the `methods` object
    methods: {
        onStepChanged(step: number) {
            // If actually clicked on something different
            // Change the route
            if (step != this.step)
                this.$router.push("/" + steps[step]);
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
