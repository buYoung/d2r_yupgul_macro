module.exports = {
    root: true,
    env: { browser: true, es2020: true },

    extends: [
        'eslint:recommended',
        'plugin:@typescript-eslint/recommended',
        'plugin:react-hooks/recommended',
        "plugin:import/recommended",
        "prettier",
    ],
    ignorePatterns: ['dist', '.eslintrc.cjs'],
    parser: '@typescript-eslint/parser',
    plugins: ['@typescript-eslint', 'prettier'],
    rules: {
        "jest/globals": "off",
        "prettier/prettier": ["warn"],
        quotes: [
            "off",
            "double",
            {
                avoidEscape: true
            }
        ],
        "@typescript-eslint/no-restricted-imports": "off",
        "@typescript-eslint/consistent-type-imports": "warn",
        "@typescript-eslint/ban-types": "off",
        "@typescript-eslint/consistent-type-exports": "off",
        "@typescript-eslint/no-explicit-any": "off",
        "@typescript-eslint/explicit-function-return-type": "off",
        "@typescript-eslint/explicit-module-boundary-types": "off",
        "@typescript-eslint/no-empty-function": "off",
        "@typescript-eslint/no-non-null-assertion": "off",
        "@typescript-eslint/no-var-requires": "off",
        "@typescript-eslint/no-unused-vars": "off",
        "@typescript-eslint/space-before-blocks": "off",
        "@typescript-eslint/no-extra-semi": "off",
        "@typescript-eslint/indent": [
            "off",
            4,
            {
                SwitchCase: 1,
                MemberExpression: 1,
                FunctionDeclaration: { parameters: "first" },
                StaticBlock: { body: 1 },
                CallExpression: { arguments: "first" },
                ArrayExpression: "first",
                ObjectExpression: "first",
                ImportDeclaration: "first",
                flatTernaryExpressions: false
            }
        ],
        "@typescript-eslint/space-infix-ops": "off",
        "@typescript-eslint/comma-dangle": [
            "off",
            {
                arrays: "always-multiline",
                objects: "always-multiline",
                imports: "never",
                exports: "never",
                functions: "never"
            }
        ],
        "@typescript-eslint/comma-spacing": [
            "off",
            {
                before: false,
                after: true
            }
        ],
        "@typescript-eslint/keyword-spacing": [
            "off",
            {
                overrides: {
                    while: { after: false },
                    if: { after: false }
                },
                before: true,
                after: true
            }
        ],
        "@typescript-eslint/semi": ["off", "always"],
        "@typescript-eslint/no-shadow": "off",
        "@typescript-eslint/ban-ts-comment": "off",
        "import/extensions": "off",
        "import/no-unresolved": "off",
        "import/order": "off",
        "import/named": 'off',
        "import/no-named-as-default": 'off',
        "react-hooks/exhaustive-deps": "off",
        "react-hooks/rules-of-hooks": "off",
        "no-restricted-imports": "off",
        "no-shadow": "off",
        "no-undef": "off",
        "no-extend-native": "off",
        "arrow-body-style": "off",
        "prefer-arrow-callback": "off",
        "max-statements-per-line": ["error", { max: 2 }],
        "multiline-ternary": ["off", "always-multiline"],
        "newline-per-chained-call": ["off", { ignoreChainWithDepth: 2 }],
        "no-mixed-spaces-and-tabs": ["off", "smart-tabs"],
        "no-tabs": ["off"],
        "operator-linebreak": ["off", "after"],
        semi: "off",
        "yield-star-spacing": ["off", "after"],
        "no-extra-semi": "off",
        "semi-spacing": [
            "off",
            {
                before: false,
                after: true
            }
        ],
        "semi-style": ["off", "last"],
        "space-before-blocks": "off",
        "no-trailing-spaces": [
            "off",
            {
                ignoreComments: true,
                skipBlankLines: true
            }
        ],
        indent: "off",
        "space-infix-ops": "off",
        "linebreak-style": ["off", "unix"],
        "comma-dangle": "off",
        "comma-spacing": "off",
        "comma-style": ["off", "last"],
        "object-property-newline": ["off"],
        "block-spacing": ["off"],
        "arrow-spacing": [
            "off",
            {
                before: true,
                after: true
            }
        ],
        "array-element-newline": ["off", "consistent", { multiline: true }],
        "array-bracket-spacing": [
            "off",
            "always",
            {
                singleValue: false
            }
        ],
        "keyword-spacing": "off",
        "implicit-arrow-linebreak": ["off", "beside"],
        "no-case-declarations": "off",
        "no-empty": [
            'error',
            {
                "allowEmptyCatch": true
            }
        ],
        "no-prototype-builtins": "off",
        "no-useless-escape": "off",
    },
}
