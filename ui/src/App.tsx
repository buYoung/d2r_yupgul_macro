import { Box, Grid, Typography } from "@mui/material";
import GemCraft from "@components/GemCraft";
import { useCallback, useEffect, useState } from "react";
import { gemCraftStore } from "@components/GemCraft.store.ts";

function App() {
    const [isReady, setIsReady] = useState(false);

    const handlePywebviewReady = useCallback(async () => {
        // @ts-ignore
        const defaultHotkeys = (await window.pywebview.api.get_default_hot_keys()).gem_craft as string[];

        console.log("defaultHotkeys", defaultHotkeys);

        if (defaultHotkeys.length === 2) {
            gemCraftStore.getState().setHotKey(`${defaultHotkeys[0]} + ${defaultHotkeys[1]}`);
            gemCraftStore.getState().setDefaultHotKey(`${defaultHotkeys[0]} + ${defaultHotkeys[1]}`);
        } else if (defaultHotkeys.length === 1) {
            gemCraftStore.getState().setHotKey(`${defaultHotkeys[0]}`);
            gemCraftStore.getState().setDefaultHotKey(`${defaultHotkeys[0]}`);
        }
    }, []);

    useEffect(() => {
        setIsReady(true);
        window.addEventListener("pywebviewready", handlePywebviewReady);
        return () => {
            window.removeEventListener("pywebviewready", handlePywebviewReady);
        };
    }, []);

    return (
        <div>
            {isReady ? (
                <div>
                    <Box
                        sx={{
                            display: "flex",
                            flexDirection: "row",
                            justifyContent: "center",
                            alignItems: "center"
                        }}>
                        <Typography
                            variant="h4"
                            sx={{
                                mr: 1
                            }}>
                            전용 큐브 매크로
                        </Typography>
                        <Typography variant="h4">v0.0.2</Typography>
                    </Box>
                    <Box
                        sx={{
                            display: "flex",
                            flexDirection: "row",
                            justifyContent: "center",
                            alignItems: "center",
                            mb: 2
                        }}>
                        <Typography variant="subtitle1">종료: Shift + ESC</Typography>
                    </Box>
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
                </div>
            ) : (
                <Box>
                    <h1>로딩중</h1>
                </Box>
            )}
        </div>
    );
}

export default App;
