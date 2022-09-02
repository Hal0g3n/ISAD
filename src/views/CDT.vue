<template>
    <div class = "CDT">
        <h1 class="subheading grey--text">CDT</h1>

        <center>

            <ImageChooser 
                name="image-chooser" 
                displayName="testing" 
                @change="uploadFile" 
                :error="error" 
                :progress="progress" 
                style="height:50vmin; width:50vmin;"
                :baseSrc=image
                />

        </center>
    </div>
</template>



<script>
import Vue from "vue";
import ImageChooser from "@/components/ImageChooser.vue";


export default Vue.extend({
    name: "HomePage",
    components: {ImageChooser},
    data: () => ({
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
