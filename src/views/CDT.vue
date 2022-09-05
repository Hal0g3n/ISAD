<template>
    <div class = "CDT"> <transition name=fade mode=out-in>
        <v-container v-if="!ready" key="Prep">
            <h1>Test Requirements</h1>
            For this test, you will require:
            <li>Blank White Paper</li>
            <li>Camera</li>
            <v-btn class="primary" style="margin-top:3vmin" @click="()=>ready=true">Ready!</v-btn>
        </v-container>

        <v-container v-else key="CDT">
            <h1 class="subheading grey--text">Clock Drawing Test</h1>

            Without referencing anything, draw a analog clock showing 10 past 11. <br/>
            Then upload a picture of the drawn clock.

            <center>

                <ImageChooser 
                    name="image-chooser" 
                    displayName="Upload Clock Image" 
                    @change="uploadFile" 
                    :error="error" 
                    :progress="progress" 
                    style="height:50vmin; width:50vmin;"
                    :baseSrc=image
                    />

            </center>

        </v-container>

    </transition> </div>
</template>



<script>
import Vue from "vue";
import ImageChooser from "@/components/ImageChooser.vue";


export default Vue.extend({
    components: {ImageChooser},
    data: () => ({
        ready: false,
        progress: null,
        error: null,
        image: null
    }),
    methods: {
        uploadFile(file) {
            // Checks if file is actually an image
            if (file.file.type.substring(0, 5) != "image") {
                console.log("KMS");
                this.error = "File is not an image";
                return;
            }

            this.error = null;
            console.log(file.file.stream());

            this.progress = 0;
            var anim = setInterval(() => {
                if (this.progress >= 100) {
                    this.progress == null;
                    clearInterval(anim);
                    this.$emit("complete", "Recall");
                }
                else this.progress += 1;
            }, 10);
        }
    }
});

</script>



<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.25s ease-out;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>