
BAICHUAN = 'baichuan-inc/Baichuan-13B-Base'
L2_ORCA = 'OpenAssistant/llama2-13b-orca-8k-3319'
L2_OPENCHAT = 'openchat/openchat_v3.1'

L2_OPENCHAT_V2 = 'openchat/openchat_v3.2'
L2_VOICELAB = 'Voicelab/trurl-2-13b'
L2 = 'TheBloke/Llama-2-13B-fp16'
L2_ORCA_CIRCULUS = 'circulus/Llama-2-13b-orca-v1'
L2_OPEN_ORCA = 'Open-Orca/OpenOrcaxOpenChat-Preview2-13B'
L2_HERMES = 'NousResearch/Nous-Hermes-Llama2-13b'
L2_WIZARD_UNCENSORED = 'ehartford/WizardLM-1.0-Uncensored-Llama2-13b'
L2_GUANACO_70B = 'TheBloke/llama-2-70b-Guanaco-QLoRA-fp16'
FALCON_40B = 'tiiuae/falcon-40b'
L2_ORCA_7B = 'circulus/Llama-2-7b-orca-v1'
L2_VICUNA_7B = 'lmsys/vicuna-7b-v1.5'
L2_HERMES_7B = 'NousResearch/Nous-Hermes-llama-2-7b'
EMOJI_TO_INT = {
    r'\u0031\ufe0f\u20e3': 1,
    r'\u0033\ufe0f\u20e3': 3,
    r'\u0032\ufe0f\u20e3': 2,
    r'\u0034\ufe0f\u20e3': 4,
    r'\u0035\ufe0f\u20e3': 5,
    r'\u0036\ufe0f\u20e3': 6,
    r'\u0037\ufe0f\u20e3': 7,
    r'\u0038\ufe0f\u20e3': 8,
    r'\u0039\ufe0f\u20e3': 9,
    r'\U0001f51f': 10,
}

capture_emojis_pattern = r'|'.join(
    [fr'(?:{code})' for code in EMOJI_TO_INT.keys()])

ALL_DIMENSIONS = ['authority', 'consensus',
                  'consistency', 'scarcity', 'unity', 'liking', 'reciprocity']

ALL_LLMS = [BAICHUAN, L2_OPENCHAT, L2_OPENCHAT,
            L2_VOICELAB, L2, L2_VICUNA_7B, L2_HERMES_7B]

LLM_ABBR_MAP = {
    'OpenAssistant/llama2-13b-orca-8k-3319': 'BAICHUAN',
    'openchat/openchat_v3.1': 'L2_OPENCHAT',
    'baichuan-inc/Baichuan-13B-Base': 'L2_ORCA',
    'Voicelab/trurl-2-13b': 'L2_VOICELAB',
    L2_VICUNA_7B: 'L2_VICUNA_7B',
    L2_HERMES_7B: 'L2_HERMES_7B'
}

DEFAULT_TEMPLATE_V2 = 'task:\n{prompt}\nYour rating: '
DEFAULT_TEMPLATE_V3 = 'Task:\n{prompt}Respond with a rating from 1 through 10 and nothing else.\nRating: '
DEFAULT_TEMPLATE_V4 = 'Task:\n{prompt}Respond with a rating from 1 through 10 and nothing else.\nRating:\n'
CHAT_TEMPLATE_V2 = 'task:\n{prompt}\nEND OF SAMPLE. Now, output the rating as an integer from 1-10:\n'
GUANACO_TEMPLATE_V2 = "task:\n{prompt}\n### Assistant: Rating: "
VICUNA_TEMPLATE_V2 = 'User: {prompt} Assistant:Rating: ',
VOICELAB_TEMPLATE = '<s>[INST]{prompt}\nRespond with a rating from 1 through 10 and nothing else.[/INST] gpt response </s> Rating: '
FALCON_40B_TEMPLATE = "Task: {prompt}\nRespond with a rating from 1 through 10 and nothing else.\nRating: "
WIZARD_UNCENSORED_TEMPLATE = "You are a helpful AI assistant.\n\nUSER: {prompt}\nRespond with a rating from 1 through 10 and nothing else.\nASSISTANT:\nRating: "
GUANACO_70B_TEMPLATE = "### Human: {prompt}\nRespond with a rating from 1 through 10. ### Assistant:\nRating: "

###### CURRENT TEMPLATES #######
OPENCHAT_TEMPLATE_V3 = "GPT4 User: {prompt}\nRespond with a rating from 1 through 10.<|end_of_turn|>GPT4 Assistant: Rating: "
ORCA_TEMPLATE_V2 = "<|system|>You are an objective instruction-following assistant. You must output a rating from 1-10 based on the user's criteria.</s><|prompter|>{prompt}\nRespond with a rating from 1 through 10.</s><|assistant|>Rating: "
VOICELAB_TEMPLATE_V2 = "<s>[INST] <<SYS>> You are an objective instruction-following assistant. You must output a rating from 1-10 based on the user's criteria.<</SYS>>{prompt}\nRespond with a rating from 1 through 10.[/INST]\ngpt response </s>Rating: "
NOUS_HERMES_TEMPLATE = "### Instruction:\n{prompt}\nRespond with a rating from 1 through 10 and nothing else.\n\n### Response:\nRating: "
################################
LLM_TEMPLATES_V2 = {
    # 'ai21-j2-mid': CHAT_TEMPLATE_V2,
    # 'gpt-3.5-turbo': CHAT_TEMPLATE_V2,
    # 'cohere-command-nightly': CHAT_TEMPLATE_V2,
    # 'TheBloke/wizardLM-13B-1.0-fp16': DEFAULT_TEMPLATE_V2,
    # 'timdettmers/guanaco-33b-merged': DEFAULT_TEMPLATE_V2,
    # 'meta-llama/Llama-2-13b-hf': DEFAULT_TEMPLATE_V3,
    # 'meta-llama/Llama-2-70b-hf': DEFAULT_TEMPLATE_V3,
    # 'WizardLM/WizardLM-13B-V1.2': DEFAULT_TEMPLATE_V3,
    # 'TheBloke/llama-2-70b-Guanaco-QLoRA-fp16': DEFAULT_TEMPLATE_V2,
    # 'baichuan-inc/Baichuan-13B-Base': DEFAULT_TEMPLATE_V2,
    # 'augtoma/qCammel-70-x': VICUNA_TEMPLATE_V2,
    # L2: DEFAULT_TEMPLATE_V3,
    # L2_ORCA_CIRCULUS: DEFAULT_TEMPLATE_V3,
    # L2_HERMES: HERMES_TEMPLATE_V1
    L2_ORCA: ORCA_TEMPLATE_V2,
    L2_OPENCHAT_V2: OPENCHAT_TEMPLATE_V3,
    L2_VOICELAB: VOICELAB_TEMPLATE_V2,
    L2_WIZARD_UNCENSORED: WIZARD_UNCENSORED_TEMPLATE,
    L2_HERMES: NOUS_HERMES_TEMPLATE,
    L2_GUANACO_70B: GUANACO_70B_TEMPLATE,
    FALCON_40B: FALCON_40B_TEMPLATE,
    L2_ORCA_7B: ORCA_TEMPLATE_V2,
    L2_HERMES_7B: NOUS_HERMES_TEMPLATE
}

suffix = "END OF SAMPLE. Output only the integer associated with the stage, step or sub-step level such that only a single integer between 1-90 is outputted, where Stage 7 Step 1 is integer 1, and Stage 16 Step 6 is integer 90, and all stages and steps in between follow a sequential order from 1-90. Output an integer from 1-90 representing the stage and step/sub-step the experts have decided on. Only output the integer (1-90), do not output anything else."
