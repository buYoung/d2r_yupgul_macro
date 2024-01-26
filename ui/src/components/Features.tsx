import { Card, CardContent, Typography } from "@mui/material";

export default function Features() {
    return (
        <Card sx={{ minWidth: 250, boxShadow: 5, height: "auto" }}>
            <CardContent>
                <Typography
                    variant="h5"
                    component="div"
                    sx={{
                        mb: 3
                    }}>
                    구현예정
                </Typography>
            </CardContent>
        </Card>
    );
}
