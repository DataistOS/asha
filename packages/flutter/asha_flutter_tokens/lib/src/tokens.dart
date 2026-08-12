import 'dart:ui';

class InteractionTokens {
  const InteractionTokens();
}

class TypographyTokens {
  const TypographyTokens();
}

class SpacingTokens {
  const SpacingTokens();
}

class ColorTokens {
  const ColorTokens();
  final dark900 = const Color(0xFF1A3C2B);
  final base500 = const Color(0xFF5B7F35);
  final light100 = const Color(0xFFA9C17E);
  final brand500 = const Color(0xFF532E3B);
}

class MotionTokens {
  const MotionTokens();
}

import 'package:flutter/material.dart';
class Typography_semanticTokens {
  const Typography_semanticTokens();
  final h1 = const TextStyle(fontSize: 32.0, fontWeight: FontWeight.bold);
  final body_base = const TextStyle(fontSize: 16.0, fontWeight: FontWeight.normal);
}

class Color_lightTokens {
  const Color_lightTokens();
}

class Spacing_semanticTokens {
  const Spacing_semanticTokens();
}

class Asha {
  static const interaction = InteractionTokens();
  static const typography = TypographyTokens();
  static const spacing = SpacingTokens();
  static const color = ColorTokens();
  static const motion = MotionTokens();
  static const typography_semantic = Typography_semanticTokens();
  static const color_light = Color_lightTokens();
  static const spacing_semantic = Spacing_semanticTokens();
}