import { Box, Grid } from "@mui/material";
import GemCraft from "@components/GemCraft";

function App() {
    return (
        <Box
            sx={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center"
            }}>
            <Grid container spacing={3}>
                <Grid item xs={12} sm={6} md={4} lg={4} xl={4}>
                    <GemCraft />
                </Grid>
                <Grid item xs={12} sm={6} md={4} lg={4} xl={4}>
                    <GemCraft />
                </Grid>
                <Grid item xs={12} sm={6} md={4} lg={4} xl={4}>
                    <GemCraft />
                </Grid>
            </Grid>
        </Box>
    );
}

export default App;
