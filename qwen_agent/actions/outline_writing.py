from qwen_agent.actions.base import Action

PROMPT_TEMPLATE_ZH = """
你是一个写作助手，任务是充分理解参考资料，从而完成写作。
#参考资料：
{ref_doc}

写作标题是：{user_request}

为了完成以上写作任务，请先列出大纲。回复只需包含大纲。大纲的一级标题全部以罗马数字计数。只依据给定的参考资料来写，不要引入其余知识。
"""

PROMPT_TEMPLATE_EN = """
You are a writing assistant. Your task is to complete writing article based on reference materials.

# References:
{ref_doc}

The title is: {user_request}

In order to complete the above writing tasks, please provide an outline first. The reply only needs to include an outline. The first level titles of the outline are all counted in Roman numerals. Write only based on the given reference materials and do not introduce other knowledge.
"""

PROMPT_TEMPLATE = {
    'zh': PROMPT_TEMPLATE_ZH,
    'en': PROMPT_TEMPLATE_EN,
}


class OutlineWriting(Action):

    def _run(self, user_request, ref_doc, lang: str = 'en'):
        prompt = PROMPT_TEMPLATE[lang].format(
            ref_doc=ref_doc,
            user_request=user_request,
        )
        return self._call_llm(prompt)
