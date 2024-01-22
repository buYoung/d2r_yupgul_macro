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
    const [personName, setPersonName] = useState<string[]>([]);

    const inputBoxRef = useRef<TextFieldProps>(null);

    const [setGems, setHotKey, save] = gemCraftStore((state) => [state.setGems, state.setHotKey, state.save]);

    useEffect(() => {
        setGems(personName as any);
    }, [personName]);

    const handleChange = (event: SelectChangeEvent<typeof personName>) => {
        const {
            target: { value }
        } = event;
        setPersonName(
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
        <Card sx={{ minWidth: 250 }}>
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
                        value={personName}
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
                    <TextField inputRef={inputBoxRef} defaultValue={1} fullWidth onKeyDown={handleHotkeyKeyDown} />
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
