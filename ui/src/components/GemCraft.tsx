import type { SelectChangeEvent, TextFieldProps } from "@mui/material";
import {
    TextField,
    Box,
    Button,
    Card,
    CardActions,
    CardContent,
    Chip,
    MenuItem,
    Select,
    Typography
} from "@mui/material";
import type { KeyboardEvent } from "react";
import { useEffect, useCallback, useRef, useState } from "react";
import { gemCraftStore } from "@components/GemCraft.store.ts";

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
    PaperProps: {
        style: {
            maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
            width: 250
        }
    }
};

const names = ["상급 보석", "최상급 보석"];

export default function GemCraft() {
    const [gemName, setGemName] = useState<string[]>([]);

    const inputBoxRef = useRef<TextFieldProps>(null);

    const [defaultGems, defaultHotKey] = gemCraftStore((state) => [state.defaultGems, state.defaultHotKey]);
    const [setGems, setHotKey, save] = gemCraftStore((state) => [state.setGems, state.setHotKey, state.save]);

    useEffect(() => {
        if (defaultGems.length === 0) return;
        if (defaultGems.length === 1) {
            let gemName = "";
            if (defaultGems[0] === "flawless") gemName = "상급 보석";
            else if (defaultGems[0] === "perfect") gemName = "최상급 보석";
            setGemName([gemName]);
        }
        if (defaultGems.length === 2) {
            setGemName(["상급 보석", "최상급 보석"]);
        }
    }, [defaultGems]);

    useEffect(() => {
        const hotkeyElement = inputBoxRef.current;
        if (!hotkeyElement) return;
        hotkeyElement.value = defaultHotKey;
    }, [defaultHotKey]);

    useEffect(() => {
        setGems(gemName as any);
    }, [gemName]);

    const handleChange = (event: SelectChangeEvent<typeof gemName>) => {
        const {
            target: { value }
        } = event;
        setGemName(
            // On autofill we get a stringified value.
            typeof value === "string" ? value.split(",") : value
        );
    };

    const handleSettingButton = useCallback(() => {
        save();
    }, []);

    const handleHotkeyKeyDown = useCallback((e: KeyboardEvent<HTMLDivElement>) => {
        const { key, altKey, ctrlKey, shiftKey } = e;
        const hotkeyElement = inputBoxRef.current;
        if (!hotkeyElement) return;

        e.preventDefault();

        if (altKey && key && key !== "Alt") {
            hotkeyElement.value = `ALT + ${key}`;
            setHotKey(key, "Alt");
        } else if (ctrlKey && key && key !== "Ctrl") {
            hotkeyElement.value = `CTRL + ${key}`;
            setHotKey(key, "Ctrl");
        } else if (shiftKey && key && key !== "Shift") {
            hotkeyElement.value = `SHIFT + ${key}`;
            setHotKey(key, "Shift");
        } else {
            hotkeyElement.value = key;
            setHotKey(key);
        }
    }, []);

    return (
        <Card sx={{ minWidth: 250, boxShadow: 5 }}>
            <CardContent>
                <Typography
                    variant="h5"
                    component="div"
                    sx={{
                        mb: 3
                    }}>
                    보석함 조합 매크로
                </Typography>
                <Box
                    sx={{
                        m: 1,
                        mb: 2
                    }}>
                    <Typography variant="body2">보석 선택:</Typography>
                    <Select
                        id="demo-multiple-chip"
                        multiple
                        fullWidth
                        value={gemName}
                        onChange={handleChange}
                        renderValue={(selected) => (
                            <Box sx={{ display: "flex", flexWrap: "wrap", gap: 0.5 }}>
                                {selected.map((value) => (
                                    <Chip key={value} label={value} />
                                ))}
                            </Box>
                        )}
                        MenuProps={MenuProps}>
                        {names.map((name) => (
                            <MenuItem key={name} value={name}>
                                {name}
                            </MenuItem>
                        ))}
                    </Select>
                </Box>
                <Box
                    sx={{
                        m: 1,
                        ml: 1
                    }}>
                    <Typography variant="body2">단축키 설정:</Typography>
                    <TextField inputRef={inputBoxRef} fullWidth onKeyDown={handleHotkeyKeyDown} />
                </Box>
            </CardContent>
            <CardActions>
                <Button size="large" fullWidth onClick={handleSettingButton}>
                    설정하기
                </Button>
            </CardActions>
        </Card>
    );
}
