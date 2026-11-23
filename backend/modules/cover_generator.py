"""
AI-Themed Project Cover Image Generator.
Implements U4: Generates attractive, high-resolution AI-themed banner images
with futuristic neural nodes, glowing synapses, project title, and domain badges.
"""

import io
import math
import random
import base64
from typing import Dict, Any
from PIL import Image, ImageDraw, ImageFont, ImageFilter

class CoverImageGenerator:
    """Generates high-tech AI project banners in PNG format using PIL."""

    def generate_cover_image(self, project_spec: Dict[str, Any]) -> Dict[str, Any]:
        title = project_spec.get("title", "ML/DL Project")
        p_type = project_spec.get("project_type", "Deep Learning")
        domain = project_spec.get("domain", "Artificial Intelligence")
        is_dl = "deep" in p_type.lower()

        # Canvas Dimensions
        width = 1200
        height = 630

        # Create gradient canvas
        image = Image.new("RGBA", (width, height), (7, 11, 25, 255))
        draw = ImageDraw.Draw(image)

        # 1. Background gradient (Deep Navy to Royal Violet)
        for y in range(height):
            ratio = y / height
            r = int(7 + ratio * (23 - 7))
            g = int(11 + ratio * (28 - 11))
            b = int(25 + ratio * (71 - 25))
            draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

        # 2. Glowing Tech Grid lines
        grid_overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        grid_draw = ImageDraw.Draw(grid_overlay)
        grid_step = 60
        for x in range(0, width, grid_step):
            grid_draw.line([(x, 0), (x, height)], fill=(40, 60, 120, 25), width=1)
        for y in range(0, height, grid_step):
            grid_draw.line([(y * 2, 0), (width, y * 2)], fill=(40, 60, 120, 20), width=1)
        image = Image.alpha_composite(image, grid_overlay)

        # 3. Neural Network Synapses & Glowing Nodes
        nodes_overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        nodes_draw = ImageDraw.Draw(nodes_overlay)

        # Seed pseudo-random placement based on title
        rand = random.Random(abs(hash(title)) % 100000)
        num_nodes = 35
        nodes = []
        for _ in range(num_nodes):
            nx = rand.randint(50, width - 50)
            ny = rand.randint(50, height - 50)
            radius = rand.randint(4, 9)
            nodes.append((nx, ny, radius))

        # Draw synaptic connecting lines between nearby nodes
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                x1, y1, _ = nodes[i]
                x2, y2, _ = nodes[j]
                dist = math.hypot(x2 - x1, y2 - y1)
                if dist < 180:
                    alpha = int(max(10, (1 - dist / 180) * 85))
                    line_color = (139, 92, 246, alpha) if is_dl else (59, 130, 246, alpha)
                    nodes_draw.line([(x1, y1), (x2, y2)], fill=line_color, width=1)

        # Draw glowing node circles
        for nx, ny, r in nodes:
            # Outer glow
            nodes_draw.ellipse([nx - r * 2, ny - r * 2, nx + r * 2, ny + r * 2], fill=(139, 92, 246, 30))
            # Core node
            core_color = (167, 139, 250, 220) if is_dl else (96, 165, 250, 220)
            nodes_draw.ellipse([nx - r, ny - r, nx + r, ny + r], fill=core_color)
            nodes_draw.ellipse([nx - 2, ny - 2, nx + 2, ny + 2], fill=(255, 255, 255, 255))

        image = Image.alpha_composite(image, nodes_overlay)

        # 4. Futuristic Central Card Overlay
        card_w = 950
        card_h = 360
        card_x = (width - card_w) // 2
        card_y = (height - card_h) // 2

        card_overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        card_draw = ImageDraw.Draw(card_overlay)

        # Frosted glass card backdrop
        card_draw.rounded_rectangle(
            [card_x, card_y, card_x + card_w, card_y + card_h],
            radius=20,
            fill=(17, 25, 54, 210),
            outline=(139, 92, 246, 180) if is_dl else (59, 130, 246, 180),
            width=2
        )
        image = Image.alpha_composite(image, card_overlay)

        # 5. Text & Typography
        final_draw = ImageDraw.Draw(image)

        # Load default or fallback font
        try:
            title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
            subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
            badge_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 15)
        except Exception:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            badge_font = ImageFont.load_default()

        # Header Pill Badge
        badge_text = f"✨  {p_type.upper()} ROADMAP  |  {domain.upper()}"
        pill_x = card_x + 40
        pill_y = card_y + 35
        pill_w = 380
        pill_h = 32
        final_draw.rounded_rectangle(
            [pill_x, pill_y, pill_x + pill_w, pill_y + pill_h],
            radius=16,
            fill=(43, 60, 117, 180),
            outline=(124, 58, 237, 220),
            width=1
        )
        final_draw.text((pill_x + 18, pill_y + 7), badge_text, fill=(224, 231, 255), font=badge_font)

        # Project Title (wrap if long)
        title_y = card_y + 90
        display_title = title if len(title) <= 45 else title[:42] + "..."
        final_draw.text((card_x + 40, title_y), display_title, fill=(255, 255, 255), font=title_font)

        # Subtitle / Tagline
        framework_tag = "TensorFlow 2 / Keras Deep Architecture" if is_dl else "Scikit-Learn Ensemble Pipeline"
        tagline = f"Production AI Blueprint  •  {framework_tag}  •  11 Lifecycle Phases"
        final_draw.text((card_x + 42, title_y + 55), tagline, fill=(165, 180, 252), font=subtitle_font)

        # Bottom Feature Badges
        badges = [
            ("🧠 Role-Based Prompts", (124, 58, 237)),
            ("⚡ Chained Execution", (59, 130, 246)),
            ("📊 S-BERT Retrieved", (6, 182, 212)),
            ("🔒 Responsible AI Verified", (16, 185, 129))
        ]

        bx = card_x + 40
        by = card_y + card_h - 70
        for b_text, b_col in badges:
            bw = len(b_text) * 9 + 25
            final_draw.rounded_rectangle(
                [bx, by, bx + bw, by + 34],
                radius=8,
                fill=(b_col[0], b_col[1], b_col[2], 50),
                outline=b_col,
                width=1
            )
            final_draw.text((bx + 12, by + 8), b_text, fill=(240, 245, 255), font=badge_font)
            bx += bw + 15

        # Convert to PNG buffer & Base64
        buffered = io.BytesIO()
        image.save(buffered, format="PNG", optimize=True)
        img_bytes = buffered.getvalue()
        b64_str = base64.b64encode(img_bytes).decode("utf-8")
        data_uri = f"data:image/png;base64,{b64_str}"

        return {
            "image_data_uri": data_uri,
            "image_bytes": img_bytes,
            "width": width,
            "height": height,
            "format": "PNG",
            "theme": "Deep Navy & Cyber Purple Gradient",
            "generator_mode": "Autonomous Neural Canvas Synthesis Engine (Pillow)"
        }

# Global singleton
cover_generator = CoverImageGenerator()
